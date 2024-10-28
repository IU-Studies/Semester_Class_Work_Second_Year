// Write a Java program to create an abstract class Document with properties like title and author, and an abstract method printContent(). 
// Provide subclasses Book, Article, and Report, each implementing the printContent() method to display the content specific to each type of document.

abstract class Document {
    String title;  
    String author; 

    public Document(String title, String author) {
        this.title = title;
        this.author = author;
    }

    abstract void printContent();
}

class Book extends Document {
    String content; 

    public Book(String title, String author, String content) {
        super(title, author);
        this.content = content;
    }

    @Override
    void printContent() {
        System.out.println("Book Title: " + title);
        System.out.println("Author: " + author);
        System.out.println("Content: " + content);
    }
}

class Article extends Document {
    String content; 

    public Article(String title, String author, String content) {
        super(title, author);
        this.content = content;
    }

    @Override
    void printContent() {
        System.out.println("Article Title: " + title);
        System.out.println("Author: " + author);
        System.out.println("Content: " + content);
    }
}

class Report extends Document {
    String content; 

    public Report(String title, String author, String content) {
        super(title, author);
        this.content = content;
    }

    @Override
    void printContent() {
        System.out.println("Report Title: " + title);
        System.out.println("Author: " + author);
        System.out.println("Content: " + content);
    }
}

public class DocumentTest {
    public static void main(String[] args) {
        Document book = new Book("Java Programming", "John Doe", "This book covers the basics of Java programming.");
        Document article = new Article("The Future of AI", "Jane Smith", "This article discusses advancements in artificial intelligence.");
        Document report = new Report("Quarterly Sales Report", "Emily Johnson", "This report details the sales performance for Q1.");

        book.printContent();
        System.out.println();
        article.printContent();
        System.out.println();
        report.printContent();
    }
}
