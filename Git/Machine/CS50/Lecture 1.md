Welcome:
	In our previous session, we learned about Scratch, a visual Programming Language.
	Indeed, all the essential programming concepts presented in Scratch will be utilized as you learn how to program any programming language.
	Recall that machines only understand binary. Where humans write *source code*, a list of instructions for the computer that is human readable, machines only understand what we can now call *machine code*. This machine code is a pattern of ones and zeros that produces a desired effect.
	It turns out that we can convert *source code* into machine code using a very special piece of software called a *compiler*. Today we will be introducing you to a compiler that will allow you to convert source code in the programming language C into machine code.
	Today, in addition to learning about how to code, you will be learning about how to write good code.
	Code can be evaluated upon three axes. First, *correctness* refers to "does the code run as intended?" Second, *design* refers to "how well is the code designed?" Finally, *style* refers to "how aesthetically pleasing and consistent is the code?"
Hello World:
	The integrated development environment(IDE) that is utilized for this course is Visual Studio Code, affectionately refereed to as, which can be accessed via that same url, or simply as "VS Code".
	One of the most important reasons we utilize VS Code is that it has all the software required for the course already pre-loaded on it. This course and the instructions herein were designed with VS Code in mind. Manually installing the necessary software for the course on your own computer is a cumbersome headache. Best always to utilize VS Code for assignments in this course.
	You can open VS Code at CS50.dev
Functions:
	In Scratch, we utilized the say block to display any text on the screen. Indeed, in C, we have a function called printf that does exactly this. 
	Notice our code already invokes this function:
		printf("Hello, World\n");
	A common error in C programming is the omission of a semicolon, Modify your code as follows:
		#include <studio.h>
		int main(void)
		{
			printf("hello, world\n")
		}
	In your terminal window, run make hello. You will now be met with numerous errors! Placing the semicolon back in the correct position and running make hello again, the errors go away.
	Notice also the special symbol \n in your code. Try removing those characters and *making* your program again by executing make hello. Typing ./hello in the terminal window, how did your program change? This \ character is called an *escape character* that tells the compiler that \n is a special instruction. Restore your program to the following:
		#include <stdio.h>
		int main(void)
		{
			printf("hello, world\n");
		} 
	Notice the semicolon and \n have been restored.
	The statement at the start of the code #include  <stdio.h> is a very special command that tells the compile that you want to use the capabilities of a *library* called stdio.h, a *header* file. This allows you, among many other things, to utilize the printf function. You can read about all the capabilities of this library on the manual pages. The Manual Pages provide a means by which to better understand what various commands do and how they function.
	Libraries are collections of pre-written functions that others have written in the past that we can utilize in our code.
Variables:
	Recall that in Scratch, we had the ability to ask the user "What's your name?" and say "hello" with that name appended to it.
	In C, we can do the same. Modify your code as follows:
		#include <studio.h>
		int main(void)
		{
			string answer = get_string("What's your name? ");
			printf("hello, %\n", answer);
		}
		The get_string function is used to get a string from the user. Then, the variable answer is passed to the printf function. %s tells the printf function to prepare itself to receive a string.
		Answer is a special holding place we call a *variable*. answer is of type string and can hold any string within it. There are many *data types*, such as int, bool, char, and many others
		% is a placeholder called a *format code* that tells the printf function to prepare to receive a string, answer is the string being passed to %s.
		Looking at the errors string and get_string are not recognized by the compiler. We have to teach the compiler these features by adding a library called cs50.h
		#include <cs50.h>
		#include <stdio.h>
		int main(void)
		{
			string answer = get_string("What's your name? ");
			printf("hello, %s\n", answer);
		}
		Notice that #include <cs50.h>  has been added to the top of your code.
		Now running make hello again in the terminal window, you can run your program by typing ./hello. The program now asks for your name and then says hello with your name attached, as intended.
		printf allows for many format codes. Here is a non-comprehensive list of ones you may utilize in the course:
			%c, %f, %i, %li, %s
Conditionals:
	Another building block you utilized within Scratch was that of *conditionals*. For example, you might want to do one thing if x is greater than y. Further, you might want to do something else if that condition is not met.
	We look at a few examples from Scratch.
	In C, you can assign a value to an int or integer as follows:
		int counter = 0;
	Notice how a variable called counter of type int is assigned the value of 0.
	C can also be programmed to add one to counter as follows
		counter = counter +1;
	Notice how 1 is added to the value of counter.
	This can be represented also as:
		counter = counter++;
	Notice how 1 is added to the value of counter. However the ++ is used instead of counter +1.
	You can also subtract one from counter as follows:
		counter = counter--;
	Notice how 1 is removed from the value of counter.
	Using this new knowledge about how to assign values to variables, you can program your first conditional statement.
		#include <cs50.h>
		#include <stdio.h>
		int main(void)
		{
			int x = get_int("What's x?");
			int y = (get_int("What's y?");
			if (x  < y )
			{
				printf("x is less than y\n");
			}
		}
	Notice that we create two variable, an int or integer called x and another called y. The values of these are populated using the get_int function.
	You can run your code by executing make compare in the terminal window, followed by ./compare. If you get any error messages, check your code for errors.
	*Flow charts* are a way by which you can examine how a computer program functions. Such charts can be used to examine the efficiency of our code.
	Looking at a flow chart of the above code, we can notice numerous shortcomings
	We can improve your program by coding as follows:
		#include <cs50.h>
		#include <stdio.h>
		int main(void)
		{
			int x = get_int("What's x?");
			int y = get_int("What's y?");
			if (x < y)
			{
				printf("x is less than y");
			}
			else if (x > y)
			{
				printf("x is greater than y");
			}
			else
			{
				printf ("x is equal to y\n");
			}
		}
	Notice that all potential outcomes are now accounted for.
	You can re-make and re-run your program and test it out.
	Examining this program on a flow chart, you can see the efficiency of our code design decisions.
	Where a string is a series of characters, a char is a single character.
	In the text editor, write code as follows:
	#include <cs50.h>
	#include <stdio.h>
	int main(void)
	{
		char c = get_char("Do you agree? ");
		if(c == 'Y' || c == 'y')
		{
			printf("Agreed.\n");
		}
		else if ( c == 'N' || c == 'n')
		{
			printf("Not agreed.\n");
		}
	}
	Notice that single quotes are utilized for single characters. Further, notice that == ensure that something is *equal* to something else, where a single equal sign would have a very different function in C. Finally, notice that || effectively means *or*. You can test your code by typing make agree into the terminal window, followed by ./agree.
Loops:
	We can also utilize the loops building bloc from Scratch in our C program.
	We look at a few examples from Scratch, Consider the following code:
	int counter = 3;
	while(counter > 0)
	{
		printf("meow\n");
		counter = counter -1;
	}
	Notice that this code assigns the value of 3 to the counter variable. Then, the while loop says meow and removes one from the counter for each iteration. Once the counter is not greater than zero, the loop ends.
	In your terminal window, type code meow.c and write the code as follows:
	#include <stdio.h>
	int main(void)
	{
		printf("meow\n");
		printf("meow\n");
		printf("meow\n");
	}
	Notice this does as intended but has an opportunity for better design.
		
		

		
	