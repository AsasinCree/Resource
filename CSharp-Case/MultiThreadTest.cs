using System;
using System.Linq;
using System.Text;
using System.Threading;
using System.Threading.Tasks;

namespace MultiThreadTest
{
    class Program
    {
        public static int count = 0;

        static void Main(string[] args)
        {
            Thread a = new Thread(new ThreadStart(PrintId1));
            Thread b = new Thread(new ThreadStart(PrintId2));
            a.Start();
            b.Start();
            Console.ReadLine();
        }

        static void PrintId1()
        {
            for (int i = 1000; i >= 1; i--)
            {
                ++count;
                Console.WriteLine(count);
                Thread.Sleep(2);
            }
        }
    }
}
