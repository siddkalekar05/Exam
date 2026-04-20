class DefaultValue {
    int a;
    double b;
    String c;
    boolean d;
    char e;
    static int p;
    static double q;
    static String r;
    static boolean s;
    static char t;


    void default1(){
        System.out.println("Default_values");
        System.out.println("Int : "+a);
        System.out.println("Double : "+b);
        System.out.println("String : "+c);
        System.out.println("Bolean : "+d);
        System.out.println("Char : "+e);
        System.out.println();
    }

    static void default2(){
        System.out.println("Static_Value");
        System.out.println("Int : "+p);
        System.out.println("Double : "+q);
        System.out.println("String : "+r);
        System.out.println("Bolean : "+s);
        System.out.println("Char : "+t);

    }
    public static void main(String[] args) {
        DefaultValue d = new DefaultValue();
        d.default1();
        default2();
    }
}
