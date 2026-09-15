from pathlib import Path

from analysis import (
    load_data,
    filter_data,
    calculate_statistics,
    create_bar_chart
)


def main():
    input_file = Path("data/inference_data.csv")
    output_folder = Path("output")

    output_folder.mkdir(exist_ok=True)

    filtered_file = output_folder / "filtered_data.csv"
    chart_file = output_folder / "object_count.png"

    print("=== Simple AI Inference Analyzer ===")

    try:
        data = load_data(input_file)

        threshold = float(
            input("Masukkan confidence threshold (0-1): ")
        )

        filtered_data = filter_data(
            data,
            threshold
        )

        statistics = calculate_statistics(
            filtered_data,
            len(data)
        )

        filtered_data.to_csv(
            filtered_file,
            index=False
        )

        chart_created = create_bar_chart(
            filtered_data,
            chart_file
        )

        print("\n=== Analysis Result ===")
        print(
            f"Total records: "
            f"{statistics['total_records']}"
        )
        print(
            f"Accepted records: "
            f"{statistics['accepted_records']}"
        )
        print(
            f"Average confidence: "
            f"{statistics['average_confidence']:.2f}"
        )
        print(
            f"Highest confidence: "
            f"{statistics['highest_confidence']:.2f}"
        )
        print(
            f"Lowest confidence: "
            f"{statistics['lowest_confidence']:.2f}"
        )
        print(
            f"Average inference time: "
            f"{statistics['average_inference_time']:.2f} ms"
        )

        print("\nObject counts:")
        for object_class, count in \
                statistics["object_counts"].items():
            print(
                f"- {object_class}: {count}"
            )

        print(
            f"\nFiltered data saved to: "
            f"{filtered_file}"
        )

        if chart_created:
            print(
                f"Chart saved to: "
                f"{chart_file}"
            )

    except ValueError as error:
        print(
            f"Input/Data Error: {error}"
        )

    except FileNotFoundError as error:
        print(
            f"File Error: {error}"
        )

    except Exception as error:
        print(
            f"Unexpected Error: {error}"
        )


if __name__ == "__main__":
    main()