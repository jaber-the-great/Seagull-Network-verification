# SCALE-MAMBA Input 

### Example input 

in.1, in.2, in.3 are three files containing (obfuscated) edge lists


### Instructions

Launch 3 terminals on the Linux machine (can be same or different machines)

terminal 0:

Party 0

```
cd SCALE-MAMBA
cat in.1 | ./Player.x -verbose 1 0 Programs/recover_network
```


terminal 1:

Party 1

```
cd SCALE-MAMBA
cat in.2 | ./Player.x -verbose 1 1 Programs/recover_network
```

terminal 2:

Paryt 2

```
cd SCALE-MAMBA
cat in.2 | ./Player.x -verbose 1 2 Programs/recover_network
```

You should see the following output from terminal 0

```
melody@BunnyLinux:~/SCALE-MAMBA$ cat in.1 | ./Player.x -verbose 1 0 Programs/recover_network 
+ '[' '' == 1 ']'
+ ./PlayerBinary.x -verbose 1 0 Programs/recover_network

No FHE Factories 2
Port Num Base 5000
Portnums : 
Verbose 1
maxI = 0
(Min,Max) number of ...
	(0,infty) multiplication triples
	(0,infty) square pairs
	(0,infty) bits

0
127.0.0.1
Player1.crt
P1
1
127.0.0.1
Player2.crt
P2
2
127.0.0.1
Player3.crt
P3


p=340282366920938463463374607431768211507

Using Mod2Engine system for the binary circuit processing
  - This uses Replicated sharing mod 2

Opening file Programs/recover_network/recover_network.sch
Number of online threads I will run in parallel =  1
Number of program sequences I need to load =  1
Loading program 0 from Programs/recover_network/recover_network-0.bc
All connections now done
Setting up threads
I am player 0 in thread 0
Waiting for thread 0 to be ready
I am player 0 in thread 3
I am player 0 in thread 20000
I am player 0 in thread 1
I am player 0 in thread 2
I am player 0 in thread 4
Set up player 0 in thread 20000 
Set up player 0 in thread 1 
Set up player 0 in thread 4 
Doing online for player 0 in online thread 0
Starting online phase 0
Set up player 0 in thread 0 
Set up player 0 in thread 2 
Set up player 0 in thread 3 
Signal online thread ready 0
Opening channel 0
Sacrifice Queues : thread = 0 : 0 0 0 : 10000 10000 10000 
Seconds per Mult Triple (all threads) inf : Total 0.000000 : Throughput 0.000000
Seconds per Square Pair (all threads) inf : Total 0.000000 : Throughput 0.000000
Seconds per Bit (all threads) inf : Total 0.000000 : Throughput 0.000000
Seconds per `Thing` (all threads) inf : Total 0.000000 : Throughput 0.000000
Sacrifice Queues : thread = 0 : 0 0 0 : 20000 20000 20000 
Seconds per Mult Triple (all threads) inf : Total 0.000000 : Throughput 0.000000
Seconds per Square Pair (all threads) inf : Total 0.000000 : Throughput 0.000000
Seconds per Bit (all threads) inf : Total 0.000000 : Throughput 0.000000
Seconds per `Thing` (all threads) inf : Total 0.000000 : Throughput 0.000000
Input channel 0 : Input channel 0 : Input channel 0 : Input channel 0 : received FIB from party 0: 1, 1
received FIB from party 1: 2, 2
received FIB from party 2: 3, 3
get magic output [0] = (6, 6)
get magic output [1] = (60, 60)
Closing channel 0
Compiler: ./compile-mamba.py -A -n -r -u -s Programs/recover_network
Waiting for all clients to finish
	Thread 0 terminating
Waiting for all clients to finish
Exiting online phase : 0
Sent 22 elements in 17 rounds
<b3m4>
Number instructions executed in online thread 0 is 271 
</b3m4>
Sacrifice Queues : thread = 0 : 0 0 0 : 29996 29996 29996 
Seconds per Mult Triple (all threads) inf : Total 0.000000 : Throughput 0.000000
Seconds per Square Pair (all threads) inf : Total 0.000000 : Throughput 0.000000
Seconds per Bit (all threads) inf : Total 0.000000 : Throughput 0.000000
Seconds per `Thing` (all threads) inf : Total 0.000000 : Throughput 0.000000
Sacrifice Queues : thread = 0 : 0 0 0 : 29996 29996 29996 
Seconds per Mult Triple (all threads) inf : Total 0.000000 : Throughput 0.000000
Seconds per Square Pair (all threads) inf : Total 0.000000 : Throughput 0.000000
Seconds per Bit (all threads) inf : Total 0.000000 : Throughput 0.000000
Seconds per `Thing` (all threads) inf : Total 0.000000 : Throughput 0.000000
Exiting inputs phase : thread = 0
Batch Size = (1048576,64)
	Per Second = 3.07723e+06
Batch Size = (1048576,128)
	Per Second = 4.67998e+06
Exiting square phase: thread = 0
Exiting mult phase : thread = 0
Joined Thread 0
Joined Thread 1
Batch Size = (1048576,256)
	Per Second = 5.32947e+06
Batch Size = (1048576,512)
	Per Second = 5.57774e+06
Batch Size = (1048576,1024)
	Per Second = 5.7398e+06
Exiting bit phase: thread = 0
Joined Thread 2
Joined Thread 3
Joined Thread 4
Batch Size = (1048576,2048)
	Per Second = 6.23223e+06
Best performance when L = 2048
	Per Second = 6.23223e+06
Finished Tuning: Generated 6545472 triples
Chosen L = 2048
Exiting Mod2 Triple production thread
Joined Thread 5
Total Time (with thread locking) = 1.40003 seconds
Produced a total of 29952 triples
Produced a total of 30208 squares
Produced a total of 59904 bits
End of prog

```
