class A {
    void showA() {
        System.out.println("Class A (Parent)");
    }
}

class B extends A {   // Single Inheritance (A → B)
    void showB() {
        System.out.println("Class B (Child of A)");
    }
}

class C extends B {   // Multilevel (A → B → C)
    void showC() {
        System.out.println("Class C (Child of B)");
    }
}

class D extends A {   // Another child of A
    void showD() {
        System.out.println("Class D (Child of A)");
    }
}

class E extends A {   // Another child of A
    void showE() {
        System.out.println("Class E (Child of A)");
    }
}

class InheritanceDemo {
    public static void main(String[] args) {

        System.out.println("---- Single + Multi Level Inheritance ----");
        C objC = new C();
        objC.showA();  // from A
        objC.showB();  // from B
        objC.showC();  // from C

        System.out.println("\n---- Hierarchical Inheritance ----");
        D objD = new D();
        objD.showA();
        objD.showD();

        E objE = new E();
        objE.showA();
        objE.showE();
    }
}