[[Lecture 0]]Computational Thinking:
	Welcome:
		This class is about more than computer programming.
		Indeed, this class is about problem-solving in a way that is exceedingly empowering! You will likely take the problem solving that you learn here will likely be instantly applicable to your work beyond this course and even your career.
		This course is far more about you advancing "you" from "where you are today" than hitting some imagined standard.
		Don't be scared if this is your first computer science class!
	What's Ahead:
		You will be learning this week about Scratch, a visual programming language.
		Then, in future weeks, you will learn about [[Lecture 1]]. That will look something like this:
			#include <stdio.h>
			int main(void)
			{
				printf("hello world\n");
			}
		Further as the weeks progress you will learn about [[algorithms]].
		You will learn about memory.
		You will learn about buggy code and what causes computer crashes.
		You will learn about [[data structures]] such as a hash table.
		Then, we will transition to a new, higher-level language call [[python]]. Your code will look something like this:
			print("hello, world")
		This class will give you a strong understanding of how recent programming languages developed from the earlier ones
		You will learn [[SQL]], [[HTML,JavaScript, and CSS]].
		We will also be looking at how we can use databases and third-party frameworks to build web applications.
	Community:
		You are part of a community of those taking this course at Harvard College.
		Puzzle Day and the CS50 Fair
		You can attend CS50 Lunches and CS50 Hackathon.
	Computer Science:
		Essentially, computer programming is about taking some input and creating some output - thus solving a problem. What happens in between the input and output, what we could call a black box, is the focus of this course.
		For example, we may need to take attendance for a class. We could use a system called unary to count, one finger at a time.
		Computers today count using a system called *binary*. It's from the term *binary digit* that we get a familiar term called *bit*. A *bit* is a zero or one: on or off.
		Computers only speak in terms of zeros and ones. Zeros represent *off*. Ones represent *on*. Computers are millions, and perhaps billions, of transistors that are being turned on and off.
		If you imagine using a light bulb, a single bulb can only count from zero to one.
	ASCII:
		Just as numbers are binary patterns of ones and zeros, letters are represented using ones and zeros too.
		Since there is an overlap between the ones and zeros that represent numbers and letters, the *ASCII* standard was created to map specific letters to specific numbers.
		For example, the letter A was decided to map to the number 65. 01000001 represents the number 65 in binary.
		if you received a text message, the binary under that message might represent the numbers 72, 73, and 33. Mapping these out to ASCII, your message would look as follows:
			H I !
			72 73 33
		![[ASCII.png]]
	Unicode:
		As time has rolled on, there are more and more ways to communicate via text.Since there were not enough digits in binary to represent all the various characters that could be represented by humans, the *Unicode* standard expanded the number of bits that can be transmitted and understood by computers. Unicode includes not only special character, but emoji as well.There are emoji that you probably use every day. Computer scientists faced a challenge when wanting to assign various skin tones to each emoji to allow the communication to be further personalized. in this case, the creators and contributors of emoji decide that the initial bits would be the structure of the emoji itself, followed by the skin tone.For example the Unicode for a generic thumbs up is U+1F44D. However, the following represents the same thumbs up with a different skin tone: U+1F44D U+1F3FD.More and more features are being added to the Unicode standard to represent further characters and emoji.
	Representations:
		Zeros and ones can be used to represent color.
		Red, green, and blue(called RGB) is a combination of three numbers.
		Taking our previously used 72, 73, and 33, which said HI! via text, would be interpreted by image readers as a light shade of yellow. The red value would be 72, the green value would be 73, and the blue would be 33,
		Further, zeros and ones can be used to represent images, videos, and music.
		Images are simply collections of RGB values.
		Videos are sequences of many images that are store together, just like a flipbook
		Music can be represented through MIDI data.
	[[algorithms]]: 
		Problem-solving is central to computer science and computer programming.
		Imagine the basic problem of trying to locate a single name in a phone book.
		How might you go about this?
		One approach could be to simply read from page one to the next until reaching the last page.
		Another approach could be to search two pages at a time.
		A final and perhaps better approach could be to go to the middle of the phone book and ask " Is the name I am looking for to the left or to the right?" Then, repeat this process, cutting the problem in half.
		Each of these approaches could be called algorithms. The speed of each these algorithms can be pictured as follows in what is call *big-O notation*:![[Big-0.png]]
		Notice that the first algorithm, highlighted in red, has a big-O of n because if there are 100 names in the phone book, it could take up to 100 tries to find the correct name. The second algorithm, where two pages were searched at a time, has a big-0 of 'n/2' because we searched twice as fast through the pages. The final algorithm has a big-O of log2n as doubling the problem would only result in one more step to solve the problem.
	Psuedocode:
		The ability to create *psuedocode* is central to one's success in both this class and in computer programming.
		Psuedocode is a human-readable version of your code. For example, considering the third algorithm above, we cold compose pseudocode as follows:![[psuedo.jpg]]
		Psuedocoding is such an important skill for at least two reasons. First, when you pseudocode before you create forma code, it allows you to think through the logic of your problem in advance. Second, when you pseudocode, you can later provide this information to others that are seeking to understand your coding decisions and how your code works.
		