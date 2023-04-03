package Lection1;

import java.util.ArrayList;
import java.util.List;
import java.util.concurrent.atomic.AtomicInteger;

public class Demo {
    public static void main(String[] args) {
//        List<Integer> availableDivider = findAvailableDivider(12);
//        for (Integer integer : availableDivider) {
//            System.out.println(integer);
        List<Integer> availableDivider = findSimpleNumbers(6);
        for (Integer integer : availableDivider) {
            System.out.println(integer);
        }
    }

    //    Пример линейной сложности O(n)
    public static List<Integer> findAvailableDivider(int number) {
        List<Integer> result = new ArrayList<>();
        for (int i = 1; i <= number; i++) {
            if (number % i == 0) {
                result.add(i);

            }
        }

        return result;
    }

    //    Пример квадратичной сложности O(n^2)
    public static List<Integer> findSimpleNumbers(int max) {
        int counter = 0;
        List<Integer> result = new ArrayList<>();
        for (int i = 1; i <= max; i++) {
            boolean simple = true;
            for (int j = 2; j < i; j++) {
                counter++;
                if (i % j == 0) {
                    simple = false;
                    break;
                }
            }
            if (simple) {
                result.add(i);
            }
        }

        System.out.println(counter);
        return result;
    }

    //    Пример экспоненциальной сложности
    public static double findSum(int sum) {
        int count = 0;
        int successResult = 0;
        for (int i = 1; i <= 6; i++) {
            for (int j = 1; j <= 6; j++) {
                for (int k = 1; k <= 6; k++) {
                    if (i + j + k == sum) {
                        successResult++;
                    }
                    count++;
                }
            }
        }

        return ((double) successResult) / ((double) count);
    }

    //    Пример экспоненциальной сложности
    //    Глубина рекурсии 2^n-1
    public static int fib(int position, AtomicInteger counter) {
        counter.incrementAndGet();
        if (position == 1 || position == 2) {
            return 1;
        }
        return fib(position - 1, counter) + fib(position - 2, counter);
    }
}
