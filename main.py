import finder
import xh

x = xh.ExcelHandler()
f = finder.FindMeOccurrences()

if __name__ == '__main__':
    # Words to search for in youtube videos
    # search_words = ["Library", "Librarian", "Book", "Books", "Learning", "Commons", "Reading", "Campus", "Cooke"]
    p = finder.FindMeFilePaths().get_paths()
    # Export entire channel to Excel document
    # x.export_found_to_file(
    #     finder.FindMeVideo().full_vid_list("https://www.youtube.com/user/PUNAHOUSCHOOL"),
    #     p["Desktop"] + "xh.xlsx"
    # )

    # Export timecodes from links.txt
    x.export_timecode_to_file(p["Desktop"] + "timecodes.xlsx")

    # x.export_printer_to_file(p["Desktop"] + "prints.xlsx")

    # Export collection of selected DV names to Excel file
    # find = "Variety Show"
    # x.export_collected_to_file(p["Desktop"] + f"{find}.xlsx", find)
