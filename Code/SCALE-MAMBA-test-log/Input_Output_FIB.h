/*
All rights reserved
*/
#ifndef _InputOutputFIB
#define _InputOutputFIB

/* A simple IO class which just uses standard
 * input/output to communicate values
 *
 * Whereas share values are input/output using
 * a steam, with either human or non-human form
 */

#include "Input_Output_Base.h"

#include <fstream>
using namespace std;

class Input_Output_FIB : public Input_Output_Base
{
  ifstream *inpf;
  ofstream *outf;

  bool human; // Only affects share output

public:
  Input_Output_FIB()
      : Input_Output_Base()
  {
  }


  void init(ifstream &ifs, ofstream &ofs, bool human_type)
  {
    //inpf= static_cast<std::ifstream*>(&ifs);
    inpf= &ifs;
    //outf= static_cast<std::ofstream*>(&ofs);
    outf= &ofs;
    human= human_type;
  }

  virtual long open_channel(unsigned int channel);
  virtual void close_channel(unsigned int channel);

  virtual gfp private_input_gfp(unsigned int channel);
  virtual void private_output_gfp(const gfp &output, unsigned int channel);

  virtual void public_output_gfp(const gfp &output, unsigned int channel);
  virtual gfp public_input_gfp(unsigned int channel);

  virtual void public_output_int(const long output, unsigned int channel);
  virtual long public_input_int(unsigned int channel);

  virtual void output_share(const Share &S, unsigned int channel);
  virtual Share input_share(unsigned int channel);

  virtual void trigger(Schedule &schedule);

  virtual void debug_output(const stringstream &ss);

  virtual void crash(unsigned int PC, unsigned int thread_num);
};

#endif

