class Book {
    String title;
    String author;
    double price;
    Book(String title,String author,double price){
        this.title = title;
        this.author = author;
        this.price = price;
    }
    void show(){
        System.out.println("Book_Title : "+title);
        System.out.println("Book_Author : "+author);
        System.out.println("Book_Price : "+price);
    }
    public static void main(String[] args) {
        Book b = new Book("java","james gossling",120.50);
        Book b1 = new Book("Python", "Parlo", 100.50);

        b.show();
        System.out.println();
        b1.show();
    }
}
