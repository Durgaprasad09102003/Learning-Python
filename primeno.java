class primeno
{
    public static void main(String args[])
    {
        int constant=0,i,j;

        System.out.println("prime numbers b/w 10 to 30");

        for(i=10;i<=30;i++)
        {
            for(j=2;j<=30;j++)
            {
                if((i%j==0) && (i!=j))
                {
                    constant=0;
                    break;
                }
                else
                {
                    constant=1;
                }
            }
            if (constant==1)
            {
                System.out.println(i);
            }
        }
    }
}