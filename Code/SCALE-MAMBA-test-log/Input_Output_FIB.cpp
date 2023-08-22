/*
All rights reserved
*/

#include "Input_Output_FIB.h"
#include "Exceptions/Exceptions.h"

#include <string>

ifstream g_input;

long Input_Output_FIB::open_channel(unsigned int channel)
{
  string filename;


  if (channel == 0) {
    filename = "input.txt";
    inpf->open(filename);
    cout << "testing input channel " << endl;
  } else if (channel > 0 && channel <= 10) {
    inpf = &g_input;
    filename = "/opt/melody/SCALE-MAMBA/Programs/small_loop/data/edgelist.txt";
    inpf->open(filename);
    cout << "opening input file "<< filename << " status = " << inpf->good();

  } else if (channel > 10 && channel <= 20) {
    inpf = &g_input;
    filename = "/opt/melody/SCALE-MAMBA/Programs/small_loop/data/updatelist.txt";
    inpf->open(filename);
  } else {
    filename = "output.txt";
    outf->open(filename);
    cout << "testing output channel " << endl;
  }

  if (channel <= 10) {
    if (inpf->fail()) {
      cout << "Could not find input file!" << endl;
    } else {
      cout << "Found input file " << filename << endl;
    }
  } else {
  if (outf->fail()) {
      cout << "Could not find output file!" << endl;
    } else {
      cout << "Found output file " << filename << endl;
    }
  }

  return 0;
}

void Input_Output_FIB::close_channel(unsigned int channel)
{
  //cout << "HAHA Closing channel " << channel << endl;
  inpf->close();
  outf->close();
}

gfp Input_Output_FIB::private_input_gfp(unsigned int channel)
{
    //cout << "Sleeps for 540s now.." << endl;
    //sleep(540);
    // this_thread::sleep_for(chrono::milliseconds(12000));
    //cout << "Continue.." << endl;
    //y.assign(i);

   int x = 111;
   gfp y;

    //cout << "HAHA2 opening status =  " << inpf->good() << "inpf->rdstate()  = " << inpf->rdstate()  << endl;
   if (inpf->good()) {
       // cout << "HAHA private input file inpf is good" << endl;
        (*inpf) >> x;
        y.assign(x);
        //cout << "HAHA reading "<< x << endl;
  }

  return y;
}

void Input_Output_FIB::private_output_gfp(const gfp &output, unsigned int channel)
{
  cout << "Output channel " << channel << " : ";
  output.output(cout, true);
}

gfp Input_Output_FIB::public_input_gfp(unsigned int channel)
{
  cout << "Enter value on channel " << channel << " : ";
  word x;
  cin >> x;
  gfp y;
  y.assign(x);

  // Important to have this call in each version of public_input_gfp
  Update_Checker(y, channel);

  return y;
}

void Input_Output_FIB::public_output_gfp(const gfp &output, unsigned int channel)
{
  cout << "Output channel " << channel << " : ";
  output.output(cout, true);
  cout << endl;
}

long Input_Output_FIB::public_input_int(unsigned int channel)
{
  cout << "Enter value on channel " << channel << " : ";
  long x;
  cin >> x;

  // Important to have this call in each version of public_input_gfp
  Update_Checker(x, channel);

  return x;
}

void Input_Output_FIB::public_output_int(const long output, unsigned int channel)
{
  cout << "Output channel " << channel << " : " << output;
  cout << " = 0x" << hex << output << dec << endl;
}

void Input_Output_FIB::output_share(const Share &S, unsigned int channel)
{
  (*outf) << "Output channel " << channel << " : ";
  S.output(*outf, human);
}

Share Input_Output_FIB::input_share(unsigned int channel)
{
  cout << "Enter value on channel " << channel << " : ";
  Share S;
  S.input(*inpf, human);
  return S;
}

void Input_Output_FIB::trigger(Schedule &schedule)
{
  printf("Restart requested: Enter a number to proceed\n");
  int i;
  cin >> i;

  // Load new schedule file program streams, using the original
  // program name
  //
  // Here you could define programatically what the new
  // programs you want to run are, by directly editing the
  // public variables in the schedule object.
  unsigned int nthreads= schedule.Load_Programs();
  if (schedule.max_n_threads() < nthreads)
    {
      throw Processor_Error("Restart requires more threads, cannot do this");
    }
}

void Input_Output_FIB::debug_output(const stringstream &ss)
{
  printf("%s", ss.str().c_str());
  fflush(stdout);
}

void Input_Output_FIB::crash(unsigned int PC, unsigned int thread_num)
{
  printf("Crashing in thread %d at PC value %d\n", thread_num, PC);
  throw crash_requested();
}
