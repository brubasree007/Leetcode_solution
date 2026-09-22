class Solution {
    public String reverseWords(String s) 
    {
        String[] word= s.trim().split("\\s+");
        String ans="";
        for(int i=word.length-1;i>=0;i--)
        {
            ans=ans+word[i];
            if(i!=0)
            {
                ans=ans+" ";
            }
        } 
        return ans;
    }
}
