""" Create a personal project that incorporates regex for tasks such as data validation, text processing, or
parsing logs. """

import re
from datetime import datetime

class LogAnalyzer:
    def __init__(self, log_file):
        self.log_file = log_file
        self.logs = []

    def load_logs(self):
        with open(self.log_file, 'r') as file:
            for line in file:
                if self.validate_log_entry(line):
                    self.logs.append(line.strip())

    def validate_log_entry(self, entry):
        pattern = r'^\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2} (INFO|WARN|ERROR) .*'
        return re.match(pattern, entry) is not None

    def extract_info(self):
        log_summary = {
            'INFO': 0,
            'WARN': 0,
            'ERROR': 0,
            'total_logs': len(self.logs),
            'log_entries': []
        }
        
        for entry in self.logs:
            timestamp, level, message = self.parse_log_entry(entry)
            log_summary[level] += 1
            log_summary['log_entries'].append({
                'timestamp': timestamp,
                'level': level,
                'message': message
            })
        
        return log_summary

    def parse_log_entry(self, entry):
        pattern = r'^(.*?) (INFO|WARN|ERROR) (.*)$'
        match = re.match(pattern, entry)
        if match:
            return match.groups()
        return None

    def display_summary(self, summary):
        print("Log Summary:")
        print(f"Total logs: {summary['total_logs']}")
        for level in ['INFO', 'WARN', 'ERROR']:
            print(f"{level}: {summary[level]}")
    
    def save_summary(self, summary, output_file='log_summary.csv'):
        with open(output_file, 'w') as file:
            file.write("Timestamp,Level,Message\n")
            for entry in summary['log_entries']:
                file.write(f"{entry['timestamp']},{entry['level']},{entry['message']}\n")

if __name__ == '__main__':
    analyzer = LogAnalyzer('logs/server.log')
    analyzer.load_logs()
    summary = analyzer.extract_info()
    analyzer.display_summary(summary)
    analyzer.save_summary(summary)


""" Note: To run this, you will need to create a server.log file with sample log entries. """
