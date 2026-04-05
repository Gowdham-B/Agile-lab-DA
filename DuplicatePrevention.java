//Main Code
package com.demo;

public class App {

    int[] seats = new int[5];

    
    public boolean bookSeat(int seatNo) {

        if (seatNo < 0 || seatNo >= seats.length) {
            return false; // invalid seat
        }

        if (seats[seatNo] == 1) {
            return false; // already booked
        }

        seats[seatNo] = 1;
        return true;
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
