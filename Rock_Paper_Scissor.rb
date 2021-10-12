def game
  print "Please choose one - rock, paper or scissors: "
  $input = gets.chomp

  $user_input = $input.downcase

  puts "You chose #{$user_input}."

  #defining which choice computer makes
  def computer_choice
    cc = (1 + rand(3))

    case cc
    when 1
      $choice = "rock"
    when 2
      $choice = "paper"
    when 3
      $choice = "scissors"
    end
  end

  computer_choice

  #comparing computer choice against user choice
  if $user_input == $choice
    puts "I chose #{$choice} too. It's a tie. Let's try again."
    game
  else
    if $user_input == "rock" && $choice == "paper"
      puts "I chose paper. Paper wraps rock. I win."
    elsif $user_input == "rock" && $choice == "scissors"
      puts "I chose scissors. Rock destroys scissors. You win."
    elsif $user_input == "paper" && $choice == "rock"
      puts "I chose rock. Paper wraps rock. You win."
    elsif $user_input == "paper" && $choice == "scissors"
      puts "I chose scissors. Scissors cut paper. I win."
    elsif $user_input == "scissors" && $choice == "rock"
      puts "I chose rock. Rock destroys scissors. I win."
    elsif $user_input == "scissors" && $choice == "paper"
      puts "I chose paper. Scissors cut paper. You win."
    else
      puts "I didn't understand you. Please try again."
      game
    end #end nested if statement
  end #end if statement
end #end game def

game
