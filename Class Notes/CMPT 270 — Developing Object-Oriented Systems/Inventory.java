 /* ---------------------------------------------
  * Copyright (c) 2025 University of Saskatchewan
  * All Rights Reserved
  * --------------------------------------------- */

public class Inventory {

    /**
     * The current amount of wood in the player's inventory
     */
    private int numWood;

    /**
     * Constructor for Inventory object, initialize wood resource to 0.
     */
    public Inventory()
    {
        numWood = 0;
    }

    /**
     * Add some wood to the inventory.
     * @param num the amount of wood to add
     */
    public void addWood(int num)
    {
        this.numWood += num;
    }

    /**
     * Removes some wood from inventory
     * @param num the amount of wood to remove. Excess wood beyond the current amount will be set to 0
     */
    public void removeWood(int num)
    {
        this.numWood -= num;
        if(this.numWood < 0)
        {
            this.numWood = 0;
        }
    }

    /**
     * Lookup the amount of wood currently in the inventory
     * @return the amount of wood in the inventory
     */
    public int getNumWood()
    {
        return this.numWood;
    }

    /**
     * Format and return a string representation of an inventory object
     * @return the string representation of an inventory object.
     */
    public String toString()
    {
        String output = "Inventory:\n";
        output += "\tWood: " + numWood;
        return output;
    }
}
