//Main Code
package com.demo;

public class App {

    
    public double calculatePrice(double price) {

        if (price <= 0) {
            return -1; // invalid input
        }

        double tax = price * 0.1;
        return price + tax;
    }
}




//Test
import static org.junit.jupiter.api.Assertions.*;
import org.junit.jupiter.api.Test;

public class AppTest {

    @Test
    void testValidPrice() {
        App app = new App();
        assertEquals(110.0, app.calculatePrice(100));
    }

    @Test
    void testInvalidPrice() {
        App app = new App();
        assertEquals(-1, app.calculatePrice(-10));
    }
}
