class WrapperClass {
    void Boxing(int a){
        Integer b = a;
        Integer c = Integer.valueOf(a);
        System.out.println(a+" "+b+" "+c);
    }
    void Unboxing(Integer p){
        int q = p;
        int r = p.intValue();
        System.out.println(p+" "+q+" "+r);
    }
    public static void main(String[] args) {
        WrapperClass w = new WrapperClass();
        w.Boxing(10);
        System.out.println();
        w.Unboxing(20);
    }
}
