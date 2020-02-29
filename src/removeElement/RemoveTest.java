package removeElement;

import org.junit.jupiter.api.Test;

import static org.junit.jupiter.api.Assertions.*;

class RemoveTest {
    @Test
    void testRemove1() {
        Remove remove = new Remove();
        int[] nums = {2, 3, 3, 2};
        int len = remove.removeElement(nums, 3);
        assertEquals(2, len);
        assertEquals(2, nums[0]);
        assertEquals(2, nums[1]);
    }

    @Test
    void testRemove2() {
        Remove remove = new Remove();
        int[] nums = {2, 5, 4, 3};
        int len = remove.removeElement(nums, 5);
        assertEquals(3, len);
        assertEquals(2, nums[0]);
        assertEquals(4, nums[1]);
        assertEquals(3, nums[2]);
    }
}