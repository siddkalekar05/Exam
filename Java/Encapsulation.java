class Encapsulation {
    int emp_id;
    String emp_name;
    double emp_salary;
    Encapsulation(int emp_id,String emp_name,double emp_salary ){
        this.emp_id = emp_id;
        this.emp_name = emp_name;
        this.emp_salary = emp_salary;
    }

    public int getEmp_id() {
        return emp_id;
    }
    public void setEmp_id(int emp_id) {
        this.emp_id = emp_id;
    }
    public String getEmp_name() {
        return emp_name;
    }
    public void setEmp_name(String emp_name) {
        this.emp_name = emp_name;
    }
    public double getEmp_salary() {
        return emp_salary;
    }
    public void setEmp_salary(double emp_salary) {
        this.emp_salary = emp_salary;
    }
    void display(){
        System.out.println("Emp_id : "+getEmp_id());
        System.out.println("Emp_name : "+getEmp_name());
        System.out.println("Emp_salary : "+getEmp_salary());
    }
   public static void main(String[] args) {
    Encapsulation e = new Encapsulation(1, "john", 50000.50);
    e.display();
    e.setEmp_salary(75000.50);
    System.out.println("Updated_Salary : "+e.getEmp_salary());
   }
}
