 /* ---------------------------------------------
  * Copyright (c) 2025 University of Saskatchewan
  * All Rights Reserved
  * --------------------------------------------- */

import java.util.Scanner;

public class TreePlanter {

    public static void main(String[] args) {

        // Create a new Scanner object to read user input from the console
        Scanner sc = new Scanner(System.in);
        boolean isQuit = false;

        // Create a new inventory object to keep track of collected wood
        Inventory inventory = new Inventory();
        Tree tree = null;

        // looping menu
        while(!isQuit)
        {
            // Display menu options to the user
            System.out.println("Choose an option:");
            System.out.println("1. Plant Tree");
            System.out.println("2. Chop Down Tree");
            System.out.println("3. Grow Tree");
            System.out.println("4. View Tree");
            System.out.println("5. Quit");
            System.out.println("- - - - - - - - - -");


            // Read in the user's choice for menu options
            int choice = sc.nextInt();

            // Map the user's menu selection to the corresponding action
            switch(choice)
            {
                // Plant Tree. Only works if a tree doesn't already exist.
                case 1:
                    if(tree == null) {
                        tree = new Tree();
                    }
                    else {
                        System.out.println("Error, trying to plant tree when one has already been planted.");
                    }
                    break;
                // Chop Down Tree. Only works if a tree already exists
                case 2:
                    if(tree == null) {
                        System.out.println("Error, trying to chop down a tree when one has not been planted yet.");
                    }
                    else {
                        int wood = tree.getHeight();
                        tree = null;
                        inventory.addWood(wood);
                    }
                    break;
                // Wait some time, allowing all of the trees in the forest to grow one stage
                case 3:
                    if(tree == null) {
                        System.out.println("Error, cannot grow tree that does not exist.");
                    }
                    else{
                        tree.grow();
                    }
                    break;
                // Print a string representation of the inventory and tree to the console, using the object's
                // toString() methods
                case 4:
                    System.out.println("- - - - - - - - - -");
                    System.out.println(inventory);
                    System.out.println(tree);
                    System.out.println("- - - - - - - - - -");

                    break;
                // Flip the boolean flag to quit the application.
                case 5:
                    isQuit = true;
                    break;
            }
        }
    }
}
