import java.util.Comparator;
import java.util.PriorityQueue;

public class Solution {

	public int findKthLargest(int[] nums, int k) {

		PriorityQueue<Integer> pq = new PriorityQueue<>();

		/*
		 * PriorityQueue<Integer> maxPriorityQueue = new PriorityQueue<>(Comparator.reverseOrder());
		 * pq pops the smallest by default
		 * the above code makes it pop the biggest first
		 */
		

		for (int num : nums) {
			pq.offer(num);

			if (pq.size() > k)
				pq.poll();
		}

		return pq.peek();
	}

	public static void main(String[] args) {
		Solution sol = new Solution();
		int[] a = {3,2,3,1,2,4,5,5,6};
		System.out.println(sol.findKthLargest(a, 4));
	}
}
