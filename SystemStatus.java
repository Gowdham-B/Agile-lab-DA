//Main Code
package com.demo;

public class App {

    String status = "PLACED";

    
    public boolean updateStatus(String newStatus) {

        if (newStatus == null || newStatus.isEmpty()) {
            return false;
        }

        status = newStatus;
        return true;
    }

    public String getStatus() {
        return status;
    }
}


//Test
import static org.junit.jupiter.api.Assertions.*;
import org.junit.jupiter.api.Test;

public class AppTest {

    @Test
    void testUpdate() {
        App app = new App();
        app.updateStatus("SHIPPED");

        assertEquals("SHIPPED", app.getStatus());
    }

    @Test
    void testInvalidStatus() {
        App app = new App();
        assertFalse(app.updateStatus(""));
    }
}
