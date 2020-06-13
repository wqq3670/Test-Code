import org.junit.*;

import static org.junit.Assert.*;

public class java20Test {

    public void add() {
        java20 a = new java20();
        int ret = a.add(10,20);
        System.out.println(ret);
    }
    @Test
    public void add1() {
        java20 a = new java20();
        System.out.println("类的实例化创建完成");
        int ret = a.add(10, java20.a);
        System.out.println(ret);
        java20.a++;
        System.out.println(java20.a);
    }

    @After//测试后
    public void After() {
        System.out.println("-----After-------");
    }

    @Before
    public void Before() {
        System.out.println("------Before------");
    }

    @BeforeClass //类的实例化创建前
    public static void beforeClass() {
        System.out.println("-------BeforeClass--------");
    }

    @AfterClass
    //必须是静态的
    public static void afterClass() {
        System.out.println("-------AfterClass--------");
    }
}