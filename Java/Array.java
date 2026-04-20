class Employee {
    int id;
    String name;
    double salary;


    Employee(int id, String name, double salary) {
        this.id = id;
        this.name = name;
        this.salary = salary;
    }

    void display() {
        System.out.println("ID: " + id + ", Name: " + name + ", Salary: " + salary);
    }
}

class EmployeeArrayDemo {
    public static void main(String[] args) {

        Employee[] emp = new Employee[3];

        emp[0] = new Employee(1, "Amit", 50000);
        emp[1] = new Employee(2, "Neha", 60000);
        emp[2] = new Employee(3, "Rahul", 55000);

        for (int i = 0; i < emp.length; i++) {
            emp[i].display();
        }
    }
}