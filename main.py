import finder
import xh

x = xh.ExcelHandler()
f = finder.FindMeOccurrences()

if __name__ == '__main__':
    p = finder.FindMeFilePaths().get_paths()
    z = finder.FindMeVideo()

    # Maurice J. "Sully" Sullivan
    # Kitty Sullivan Wo
    # Sullivan Administration Building (1972)
    # President's Office
    # Admissions Office
    # PFA Office
    # Business Office
    # Physical Plant
    # Development Office

    # Words to search for in YouTube videos
    search_words = [
        "Maurice",
        "Sully",
        "Sullivan",
        "Administration",
        "President",
        "Admissions",
        "PFA",
        "Business",
        "Physical Plant",
        "Development"
    ]

    # Export entire channel to Excel document
    # x.export_found_to_file(
    #     finder.FindMeVideo().full_vid_list("PUTURLHERE"),
    #     p["Desktop"] + "xh.xlsx"
    # )

    # Export timecodes from links.txt
    # x.export_timecode_to_file((p["Desktop"] + "timecodes.xlsx"), True)

    # x.export_found_to_file(
    #     z.find_from_channel(
    #         "Channel URL",
    #         search_words
    #     ),
    #     p["Desktop"] + "found.xlsx"
    # )

    # x.export_found_to_file(
    #     z.find_from_excel(p["Desktop"] + "psyl.xlsx", "pl", search_words),
    #     p["Desktop"] + "zzz.xlsx"
    # )

    # x.export_printer_to_file(p["Desktop"] + "prints.xlsx")

    # Export collection of selected DV names to Excel file
    find = "pfa"
    x.export_collected_to_file(p["Desktop"] + f"{find}.xlsx", find)
