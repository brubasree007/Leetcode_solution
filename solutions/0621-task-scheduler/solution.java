class Solution {
    public int leastInterval(char[] tasks, int n) 
    {
        int [] freq=new int[26];
        for(char c:tasks)
        {
            freq[c-'A']++;
        }
        Arrays.sort(freq);
        int max=freq[25];
        int idle=(max-1)*n;
        for(int i=24;i>=0;i--)
        {
            idle-=Math.min(max-1,freq[i]);
        }
        return tasks.length+Math.max(0,idle);
        
    }
}
