package CW2;

import java.util.ArrayList;

public class Main {
    public static void main(String[] args) {
        ToyStore shopToy = new ToyStore();
        shopToy.put(1, "Игрушка1", 0.1);
        shopToy.put(2, "Игрушка2", 0.6);
        shopToy.put(3, "Игрушка3", 0.2);
        shopToy.put(4, "Игрушка4", 0.5);
        shopToy.put(5, "Игрушка5", 0.3);
        shopToy.put(6, "Игрушка6", 0.4);
        shopToy.put(1, "Игрушка1", 0.1);
        shopToy.put(2, "Игрушка2", 0.6);
        shopToy.put(3, "Игрушка3", 0.2);
        shopToy.put(4, "Игрушка4", 0.5);
        shopToy.put(5, "Игрушка5", 0.3);
        shopToy.put(6, "Игрушка6", 0.4);

        String fileName = "CW2/result.txt";
        ArrayList<Toy> lotteryList = new ArrayList<>();
        for (int i = 0; i < 10; i++) {
            lotteryList.add(shopToy.get());
        }
        shopToy.saveArrayToFile(fileName, lotteryList);
        shopToy.saveToFile(fileName, shopToy.get());
    }

}
