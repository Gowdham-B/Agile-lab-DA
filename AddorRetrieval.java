//AddorRetrieve_record
package com.demo;

public class App {

    static class Patient {
        int id;
        String name;

        Patient(int id, String name) {
            this.id = id;
            this.name = name;
        }
    }

    Patient[] p = new Patient[10];
    int count = 0;

    public boolean addrecord(int id, String name) {
        if (id <= 0 || name == null || name.isEmpty()) {
            return false;
        }
        p[count++] = new Patient(id, name);
        return true;
    }

    public Patient getrecord(int id) {
        for (int i = 0; i < count; i++) {
            if (p[i].id == id) {
                return p[i];
            }
        }
        return null;
    }

    public static void main(String[] args) {
        System.out.print("App is running...");
    }

}








//Testcode
package com.demo;

import static org.junit.jupiter.api.Assertions.*;
import org.junit.jupiter.api.Test;

public class AppTest {
    @Test
    public void validinput() {
        App obj = new App();
        assertTrue(obj.addrecord(1, "GB"));
        assertFalse(obj.addrecord(0, ""));
    }

    @Test
    public void retrieve() {
        App obj = new App();
        obj.addrecord(1, "HH");
        App.Patient o = obj.getrecord(1);
        assertEquals("HH", o.name);
        assertFalse("PN".equals(o.name));
    }
}
