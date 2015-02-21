// 1.1 Implement an algorithm to determine if a string has all unique characters. What if you
// can not use additional data structures?
import java.util.*;
import acm.program.*;

public class UniqueCharacterTest extends ConsoleProgram {
	public void run()
	{
		while (true)
		{
			String stringForTest = readLine("Please, give a string for input: ");
			ArrayList<String> listOfChars = new ArrayList<String>();
			boolean twoLoopsFinished = false;
			for (int i = 0; i < stringForTest.length() && !twoLoopsFinished; i++)
			{
				for (int j = 0; j < listOfChars.size(); j++)
				{
					if (listOfChars.get(j).equals(Character.toString(stringForTest.charAt(i))))
					{
						twoLoopsFinished = true;
						println("Your string doesn't have all unique characters");
						break;
					}
				}

				if (listOfChars.size() == 0 || !twoLoopsFinished)
				{
					listOfChars.add(Character.toString(stringForTest.charAt(i)));
				}
			}

			if (!twoLoopsFinished)
			{
				println("Your string has all unique characters!");
			}
		}
	}
}
