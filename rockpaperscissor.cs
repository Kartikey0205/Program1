using System;

namespace Helloworld
{
    class Program
    {
        static void Main(string[] args)
        {
            string ans = "";
            int count = 0;
            int count1 = 0;

            Console.WriteLine("Welcome to RPS game");

            while (ans != "NO")
            {
                Console.WriteLine("Select any one:\n1->ROCK\n2->PAPER\n3->SCISSOR");
                string[] choices = new string[3] { "ROCK", "PAPER", "SCISSOR" };
                Random rnd = new Random();
                int n = rnd.Next(0, 3);
                Console.WriteLine("Enter your choice:");
                string user = Console.ReadLine().ToUpper();
                Console.WriteLine("Computer:" + choices[n]);

                if (user == "ROCK" && choices[n] == "SCISSOR")
                {
                    Console.WriteLine("User wins");
                    count += 1;
                }
                else if (user == "ROCK" && choices[n] == "PAPER")
                {
                    Console.WriteLine("Computer wins");
                    count1 += 1;
                }
                else if (user == "PAPER" && choices[n] == "ROCK")
                {
                    Console.WriteLine("User wins");
                    count += 1;
                }
                else if (user == "PAPER" && choices[n] == "SCISSOR")
                {
                    Console.WriteLine("Computer Wins");
                    count1 += 1;
                }
                else if (user == "SCISSOR" && choices[n] == "ROCK")
                {
                    Console.WriteLine("Computer Wins");
                    count1 += 1;
                }
                else if (user == "SCISSOR" && choices[n] == "PAPER")
                {
                    Console.WriteLine("User wins");
                    count += 1;
                }
                else
                {
                    Console.WriteLine("Same choices");
                }
                Console.WriteLine("Do u want to continue(YES/NO):");
                ans = Console.ReadLine().ToUpper();
                Console.WriteLine("---------------------------------------");
            }
            Console.WriteLine("User wins " + count + " times");
            Console.WriteLine("Computer wins " + count1 + " times");
        }
    }
}
