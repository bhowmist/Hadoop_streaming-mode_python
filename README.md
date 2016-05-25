# Hadoop_streaming-mode_python
Average sentence length - sentenceLength.sh <hdfs input file/folder> <hdfs output folder> - From all the text file(s) in the given hdfs path (such as /data/books or /data/books/PeterPan.txt), give the average sentence length over the texts.  Here our (not perfect) definition of a sentence is any sequence of characters beginning with a capital letter and ending with . ! or ? Sentence length is the number of characters between and  including the capital and punctuation.  No further computation can be done after the reducer, so all computation must be finished  in the reduce phase and limit yourself to a single reducer (default).  

eaxample input-output in command line ---

>> ./sentenceLength.sh /data/books/TSEliiot.txt eliot
….
>>hadoop fs -cat /user/<username>/eliot
SentenceCount	507
AvgSentenceLength	35.433
