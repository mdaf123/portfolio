import java.util.ArrayList;
import java.util.List;
import java.util.Scanner;
import java.util.Collections;
import java.util.HashMap;
import java.util.Map;
public class Main {	
	public static void main(String[] args) {
		List<Double> list=new ArrayList<Double>();
		Scanner scanner=new Scanner(System.in);
		System.out.println("What are all the values of your data set(seperate with commas)?");
		System.out.println("ex: 30,30.1,69.8,74.4");
		double sum = 0;
		int lengthoflist = 0;
		double standevthingy = 0;
		String value = scanner.nextLine();
		String[] values = value.split(",");
		for (String val : values) {
			try {
				double number = Double.parseDouble(val.trim());
				list.add(number);
				sum = sum+number;
				lengthoflist = lengthoflist + 1;
			} catch (NumberFormatException e) {
				System.out.println("Incorrect number format for value:" + val);
			}
		}
		for (String val: values) {
		    double number = Double.parseDouble(val.trim());
		    standevthingy = Math.pow(Math.abs((number-(sum/lengthoflist))), 2)+standevthingy;
		}
		scanner.close();
		double min = Collections.min(list);
		System.out.println("Minimum: " + min);
		double max = Collections.max(list);
		System.out.println("Maximum: " + max);
		System.out.println("Sum: " + sum);
		System.out.println("Mean/Average: " + (sum/lengthoflist));
		System.out.println("Standard Deviation: " + Math.sqrt((standevthingy/lengthoflist)));
		System.out.println("Variance: " + (standevthingy/lengthoflist));
		Collections.sort(list);
		double median;
		if (lengthoflist % 2 == 0) {
			median = (list.get(lengthoflist/2-1) + list.get(lengthoflist/2))/2.0;
		} else {
			median = list.get(lengthoflist/2);
		}
		System.out.println("Median: " + median);
        Map<Double, Integer> frequencyMap = new HashMap<>();
        for (double num : list) {
            frequencyMap.put(num, frequencyMap.getOrDefault(num, 0) + 1);
        }

        double mode = list.get(0);  // Default to the first element
        int maxFrequency = 0;
        boolean modeFound = false;

        for (Map.Entry<Double, Integer> entry : frequencyMap.entrySet()) {
            if (entry.getValue() > maxFrequency) {
                maxFrequency = entry.getValue();
                mode = entry.getKey();
                modeFound = true;
            }
        }
        if (maxFrequency == 1) {
            modeFound = false;
        }
        if (modeFound = true) {
        	System.out.println("Mode: " + mode);
        } else {
            System.out.println("Mode: none");
        }
	}

}
