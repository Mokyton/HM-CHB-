import time
import os

slide1 = """
                                       $$$$$$$$
                                $$$$$$$$$$$$$$$$$$
                             $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
                          $$$$$$$$$$$$$$$$ $      $$$$$$$$$$$$$$$$$$$
                        $$$$$$$$$$$               $$ $$$$$$$$$$$$$$$$$$
                       $$$$$$$$ $$$                    $$$$$$$$$$$$$$$$$
             $$$$$$$  $$$$$$$                   $$$$$  $$$$$$$$$$$$$$$$$$
         $$$$$$$$$$$$$$$$$$$        $          $$$$$$$  $$$$$$$$$$$$$$$$$
       $$$$$$$$$$$$$$$$$$$$      $$$$$$$       $$$$$$$  $$$$$$$$$$$$$$$$$$
     $$$$$$$$$$$$$$$$$$$$$$     $$$$$$$$        $$$$$   $$$$$$$$$$$$$$$$$$
    $$$$$$$$$$$$$$$$$$$$$$$      $$$$$$$     $$$        $$$$$$$$$$$$$$$$$$
   $$$$$$$$$$$$$$$$$$$$$$$$$        $                  $$$$$$$$$$$$$$$$$$ 
  $$$$$$$$$$$$$$$$$$$$$$$$$$                   $      $$$$$$$$$$$$$$$$$$
 $$$$$$$$$$$$$$$$$$$$$$$$$$$$$                      $$$$$$$$$$$$$$$$$$
 $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$            $$$$$ $$$$$$$$$$$$$$$$$$$
  $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
  $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$ $$$$$$$$$$$$$$$$
   $$$$$$$$$$$$$$$$$$$$$$$$$$ $$ $$ $  $$$$$$$$$$$$$$$$$$$$$
    $$$$$$$$$$$$$$$$$$$$$$$$$   $ $$$$$$$    $$ $$$$$$$$$$$$
     $$$$$$$$$$$$$$$$$$$$$   $$$$$$$$      $ $$$$$$$$$$$$$$
        $$$$$$$$$$$$$$$     $$$$$$$$$$    $  $$$$$ $$$$$$$
              $$$          $$$$ $$$$  $$ $ $$$$$ $$$$$
                            $$$$ $$$  $   $ $$ $$$$ $$
                            $$$$$$$     $ $ $$$$$$$$$$$
                             $$$$$$ $$$  $ $$$$$$$$$$$$
                               $$$$$$$$$$$$$$$$$$$$$$$
                                $$$$$$$$$$$$$$$$$$$$$$
                              $$$$$$$$$$$$$$$$$$$$$ $$$$
                            $$$$$$$$$$$$$$$$ $$$$$$$$$$$$
                           $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
                           $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
"""

slide2 = """
                                       $$$$$$$$
                                $$$$$$$$$$$$$$$$$$
                             $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
                          $$$$$$$$$$$$$$$$ $      $$$$$$$$$$$$$$$$$$$
                        $$$$$$$$$$$               $$ $$$$$$$$$$$$$$$$$$
                       $$$$$$$$ $$$                    $$$$$$$$$$$$$$$$$
                   $  $$$$$$$                   $$$$$  $$$$$$$$$$$$$$$$$$
               $$$$$$$$$$$$$                   $$$$$$$  $$$$$$$$$$$$$$$$$
             $$$$$$$$$$$$$$    $$$$$$$$        $$$$$$$  $$$$$$$$$$$$$$$$$$
           $$$$$$$$$$$$$$$$     $$$$$$$$        $$$$$   $$$$$$$$$$$$$$$$$$
          $$$$$$$$$$$$$$$$$                             $$$$$$$$$$$$$$$$$$
         $$$$$$$$$$$$$$$$$$$       $$                  $$$$$$$$$$$$$$$$$$ 
        $$$$$$$$$$$$$$$$$$$$         $$$              $$$$$$$$$$$$$$$$$$
       $$$$$$$$$$$$$$$$$$$$$$$          $$$$$$      $$$$$$$$$$$$$$$$$$
       $$$$$$$$$$$$$$$$$$$$$$$$$                  $$$$$$$$$$$$$$$$$$$
        $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
        $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$ $$$$$$$$$$$$$$$$
         $$$$$$$$$$$$$$$$$$$$ $$ $$ $  $$$$$$$$$$$$$$$$$$$$$
          $$$$$$$$$$$$$$$$$$$   $ $$$$$$$    $$ $$$$$$$$$$$$
           $$$$$$$$$$$$$$$   $$$$$$$$      $ $$$$$$$$$$$$$$
              $$$$$$$$$     $$$$$$$$$$    $  $$$$$ $$$$$$$
                    $$$    $$$$ $$$$  $$ $ $$$$$ $$$$$
                            $$$$ $$$  $   $ $$ $$$$ $$
                            $$$$$$$     $ $ $$$$$$$$$$$
                             $$$$$$ $$$  $ $$$$$$$$$$$$
                               $$$$$$$$$$$$$$$$$$$$$$$
                                $$$$$$$$$$$$$$$$$$$$$$
                              $$$$$$$$$$$$$$$$$$$$$ $$$$
                            $$$$$$$$$$$$$$$$ $$$$$$$$$$$$
                           $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
                           $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
"""

slides = [slide1, slide2, slide1, slide2, slide1, slide2, slide1, slide2]
for i in slides:
  os.system('cls')
  print(i, end='\r')
  time.sleep(1)
 


