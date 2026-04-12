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
package com.demo;

import static org.junit.jupiter.api.Assertions.*;
import org.junit.jupiter.api.Test;

public class AppTest {

    
    @Test
    void testValidBooking() {
        App app = new App();
        assertTrue(app.bookSeat(2));
    }

    
    @Test
    void testDuplicateBooking() {
        App app = new App();

        app.bookSeat(2); // first booking
        assertFalse(app.bookSeat(2)); // duplicate
    }

    
    @Test
    void testInvalidSeatNegative() {
        App app = new App();
        assertFalse(app.bookSeat(-1));
    }

    
    @Test
    void testInvalidSeatOutOfRange() {
        App app = new App();
        assertFalse(app.bookSeat(10));
    }
}
