<html>
        <body>
            <?php
                error_reporting(E_ALL);
                session_start();

                $_SESSION['username'] = true;// to bypass Login page (remove it once you test it)

                if(!isset($_POST['user_choice'])){
                    if(!isset($_SESSION['username'])){
                        header('location:login.php');
                    }
                    else{
                        echo "First page:";
                        $_SESSION['secondPage'] = true;
                        echo '<form action=htmlspecialchars($_SERVER["PHP_SELF"]); method="post" />
                        <input type="radio" name="user_choice" value="Rock" title="Rock" />Rock <br /><br />
                        <input type="radio" name="user_choice" value="Paper" title="Paper" />Paper <br /><br />
                        <input type="radio" name="user_choice" value="Scissors" title="Scissors" />Scissors <br /><br />
                        <input type="submit" name="form_submit" value="submit"/> 
                        </form> ';
                    }
                }
            ?>
            <?php
                if(!isset($_SESSION['username'])) {
                    header('location:login.php');
                } else {
                    if(isset($_POST['user_choice'])) {
                        echo "Second Page:<br><br>";
                        $CPUChoice = array('Rock', 'Paper', 'Scissors');
                        shuffle($CPUChoice);
                        //echo "CPU Select". $CPUChoice[0];exit;

                        $CPU = $CPUChoice[0];
                        $User = $_POST['user_choice'];

                        echo 'Player: '.$User.' <br>CPU: '.$CPU;

                        if($User === $CPU){
                            echo '<br>Result: Tie!';
                        }
                        else if($User === "Rock"){
                            if($CPU === "Scissors") {
                                echo '<br>Result: User wins';
                            } else {
                                echo '<br>Result: CPU wins';
                            }
                        }
                        else if($User === "Paper") {
                            if($CPU === "Rock") {
                                echo '<br>Result: User wins';
                            }else {
                                if($CPU === "Scissors") {
                                    echo '<br>Result: Computer wins';
                                }
                            }
                        }
                        else if($User === "Scissors") {
                            if($CPU === "Rock") {
                                echo '<br>Result: CPU wins';
                            } else {
                                if($CPU === "Paper") {
                                    echo '<br>Result: User wins';
                                }
                            }
                        }
                   }
                }
            ?>
        </body>
    </html>
