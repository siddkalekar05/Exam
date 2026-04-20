class Employe {
    int id;
    String name;
    double salary;
    Employe(int id,String name,double salary){
        this.id = id;
        this.name=name;
        this.salary=salary;
    }
    void display(){
        System.out.println("Employe_id : "+id);
        System.out.println("Employee_name = : "+name);
        System.out.println("Employee_salary : "+salary);
    }  
}
class Test{
    public static void main(String[] args) {
        Employe e = new Employe(1,"John",75000.50);
        e.display();
    }
}
