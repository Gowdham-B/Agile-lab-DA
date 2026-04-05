//Main Code
package com.demo;

public class App {


public boolean validateCoupon(String code) {

     if (code == null || code.isEmpty()) {
          return false;
     }

     if (code.equals("SAVE10")) {
          return true;
     }

     return false;
}

public static void main(String[] args) {
     System.out.print("App is running...");
}

}



//Test code
package com.demo;
import static org.junit.jupiter.api.Assertions.*;
import org.junit.jupiter.api.Test;

public class AppTest {

    @Test
    void testValidCoupon() {
        App app = new App();
        assertTrue(app.validateCoupon("SAVE10"));
    }

    @Test
    void testInvalidCoupon() {
        App app = new App();
        assertFalse(app.validateCoupon("ABC"));
    }

    @Test
    void testEmptyCoupon() {
        App app = new App();
        assertFalse(app.validateCoupon(""));
    }
}
