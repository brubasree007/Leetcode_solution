class Solution {
    public List<Integer> partitionLabels(String s) 
    {
        List<Integer> par=new ArrayList<>();
        for(int i=0;i<s.length();)
        {
            int start=i;
            int end=s.lastIndexOf(s.charAt(start));
            for (int j=start+1;j<=end;j++)
            {
                int last=s.lastIndexOf(s.charAt(j));
                if(last>end)
                {
                    end=last;
                }
            }
            par.add(end-start+1);
            i=end+1;
        }
        return par;
    }
}
