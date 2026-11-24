import { render, screen } from "@testing-library/react";
import HomePage from "./page";

describe("HomePage", () => {
  it("renders the product heading", () => {
    render(<HomePage />);
    expect(
      screen.getByRole("heading", { level: 1, name: "Safarnama" }),
    ).toBeInTheDocument();
  });

  it("states that no travel data is available yet", () => {
    render(<HomePage />);
    expect(
      screen.getByText(/no travel data is available yet/i),
    ).toBeInTheDocument();
  });
});
