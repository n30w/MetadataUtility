import finder
import xh

x = xh.ExcelHandler()

if __name__ == '__main__':
    # Words to search for in youtube videos
    search_words = ["Library", "Librarian", "Book", "Books", "Learning", "Commons", "Reading", "Campus", "Cooke"]

    # Export entire channel to excel document
    x.export_found_to_file(finder.FindMe().full_list(), "/Users/neoalabastro/Desktop/xh.xlsx")

    # Export timecodes from links.txt
    x.export_timecode_to_file("/Users/neoalabastro/Desktop/timecodes.xlsx")
