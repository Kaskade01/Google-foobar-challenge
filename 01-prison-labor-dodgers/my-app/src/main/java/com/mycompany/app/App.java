package com.mycompany.app;
import java.util.HashMap;
import java.util.Set;

/**
 * Hello world!
 *
 */
public class App 
{
    public static void main( String[] args )
    {
        int x[] = {14, 27, 1, 4, 2, 50, 3, 1, -4, 82};
        int y[] = {2, 4, -4, 3, 1, 1, 14, 27, 50};
        System.out.println(answer(x, y));
    }

    
    public static int answer(int[] x, int[] y){
        int answer = 9999; // answer cannot be 9999
        HashMap<Integer, Integer> lookupTable = new HashMap<Integer, Integer>();

        // count each occurence of a number in X array and save its count in a map
        for(int id_number : x){
            Integer id_key = Integer.valueOf(id_number);
            if(lookupTable.containsKey(id_key)){
                int current_value = lookupTable.get(id_key).intValue();
                lookupTable.put(id_key, Integer.valueOf(current_value + 1));
            } else {
                lookupTable.put(id_key, Integer.valueOf(1));
            }
        }

        // keep counting numbers in Y array
        for(int id_number : y){
            Integer id_key = Integer.valueOf(id_number);
            if(lookupTable.containsKey(id_key)){
                int current_value = lookupTable.get(id_key).intValue();
                lookupTable.put(id_key, Integer.valueOf(current_value + 1));
            } else {
                lookupTable.put(id_key, Integer.valueOf(1));
            }
        }

        // find the answer
        Set<Integer> id_keys = lookupTable.keySet();
        for(Integer id : id_keys){
            if(lookupTable.get(id).intValue() % 2 != 0){
                return id.intValue();
            }
        }
        return answer; // this return would be an error
    }
}
