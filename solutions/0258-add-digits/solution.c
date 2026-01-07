int addDigits(int num) 
{
    int rem,res;
    while(num>=10)
    {
        res=0;
        while(num!=0)
        {
            rem=num%10;
            res+=rem;
            num/=10;
        }
        num=res;
    }
    return res;

}

