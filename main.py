import finder
import xh

x = xh.ExcelHandler()
f = finder.FindMeOccurrences()

if __name__ == '__main__':
    # Words to search for in youtube videos
    # search_words = ["Library", "Librarian", "Book", "Books", "Learning", "Commons", "Reading", "Campus", "Cooke"]

    # Export entire channel to Excel document
    #x.export_found_to_file(finder.FindMeVideo().full_vid_list("https://www.youtube.com/user/PUNAHOUSCHOOL"),
# "/Users/neoalabastro/Desktop/xh.xlsx")

    # Export timecodes from links.txt
    # x.export_timecode_to_file("/Users/neoalabastro/Desktop/timecodes.xlsx")

    # x.export_printer_to_file("/Users/neoalabastro/Desktop/prints.xlsx")

    # Export collection of selected DV names to Excel file
    find = "Variety Show"
    x.export_collected_to_file(f"/Users/neoalabastro/Desktop/{find}.xlsx", find)