 /* ---------------------------------------------
 * Copyright (c) 2025 University of Saskatchewan
 * All Rights Reserved
 * --------------------------------------------- */

public class Tree {

    /**
     * The height or growth stage of the tree
     */
    private int height;

    /**
     * Constructor to create a new Tree object.
     * Initialize the tree's height as 0 (representing a sapling)
     */
    public Tree()
    {
        this.height = 0;
    }

    /**
     * Grow the tree by one growth stage.
     */
    public void grow()
    {
        this.height++;
    }

    /**
     * Lookup the height of the tree
     * @return an integer representing the height or growth stage of the tree
     */
    public int getHeight()
    {
        return this.height;
    }

    /**
     * Returns a formatted String representation of this object.
     * @return a String formatted to describe the current state of this object.
     */
    public String toString() {
        String s = "Tree Height: " + this.height + "\n";
        return s;
    }
}