class NumberContainers {

    private Map<Integer, Integer> idxToNum;

    private Map<Integer, TreeSet<Integer>> numToIdx; // java version of sorted set

    public NumberContainers() {
        idxToNum = new HashMap<>();
        numToIdx = new HashMap<>();
    }
    
    public void change(int index, int number) {
        if (idxToNum.containsKey(index)) {
            int oldno = idxToNum.get(index);
            TreeSet<Integer> oldset = numToIdx.get(oldno);
            oldset.remove(index);

            if (oldset.isEmpty()) {
                numToIdx.remove(oldno);
            }
        }

        idxToNum.put(index, number);

        TreeSet<Integer> set = numToIdx.get(number);
        if (set == null) {
            set = new TreeSet<>();
            numToIdx.put(number, set);
        }
        set.add(index);
    }
    
    public int find(int number) {
        if (numToIdx.containsKey(number) && !numToIdx.get(number).isEmpty()) {
            return numToIdx.get(number).first();
        }

        return -1;
    }
}

/**
 * Your NumberContainers object will be instantiated and called as such:
 * NumberContainers obj = new NumberContainers();
 * obj.change(index,number);
 * int param_2 = obj.find(number);
 */