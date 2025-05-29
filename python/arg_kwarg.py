class Asset:
    def __init__(self, asset_id: str, purchase_date: str, *args, **kwargs):
        """
        Initializes a generic asset.
        *args can capture any extra positional arguments.
        **kwargs can capture any extra keyword arguments (e.g., location, condition).
        """
        self.asset_id = asset_id
        self.purchase_date = purchase_date

        # Store any additional keyword arguments as attributes or in a dict
        self.additional_info = kwargs
        self.extra_positional_args = (
            args  # Less common for __init__ to use *args this way
        )

        print(f"--- Initializing Asset ---")
        print(f"  Asset ID: {self.asset_id}")
        print(f"  Purchase Date: {self.purchase_date}")
        if self.extra_positional_args:
            print(f"  Extra Positional Args for Asset: {self.extra_positional_args}")
        if self.additional_info:
            print(f"  Additional Asset Info (from kwargs): {self.additional_info}")
        print(f"--- Asset Initialized ---\n")

    def get_description(self, *args, **kwargs) -> str:
        """
        Returns a basic description of the asset.
        Subclasses can override this and pass through args/kwargs.
        """
        desc = f"Asset ID: {self.asset_id}, Purchased: {self.purchase_date}"
        if "short_desc" in kwargs and kwargs["short_desc"]:
            return f"Asset: {self.asset_id}"
        if self.additional_info:
            desc += f", Info: {self.additional_info}"
        if args:  # Extra args passed directly to this method call
            desc += f", Method Args: {args}"
        return desc


class Computer(Asset):
    def __init__(
        self,
        asset_id: str,
        purchase_date: str,
        cpu_type: str,
        ram_gb: int,
        *args,
        **kwargs,
    ):
        """
        Initializes a Computer asset.
        It accepts its own specific arguments (cpu_type, ram_gb)
        and uses *args and **kwargs to pass any other arguments
        (like location, condition, or any future Asset arguments)
        up to the Asset parent class constructor.
        """
        print(f"--- Initializing Computer (Subclass of Asset) ---")
        # Call the parent class's __init__ method
        # We explicitly pass asset_id and purchase_date.
        # *args and **kwargs will forward any OTHER arguments to the Asset constructor.
        super().__init__(asset_id, purchase_date, *args, **kwargs)

        self.cpu_type = cpu_type
        self.ram_gb = ram_gb

        print(f"  Computer Specifics - CPU: {self.cpu_type}, RAM: {self.ram_gb}GB")
        print(f"--- Computer Initialized ---\n")

    def get_description(self, include_specs: bool = True, *args, **kwargs) -> str:
        """
        Overrides the parent's get_description to include computer-specific details.
        It also demonstrates forwarding *args and **kwargs to the parent's method.
        """
        # Get the base description from the parent class
        # Pass through any *args or **kwargs meant for the parent's get_description
        base_desc = super().get_description(*args, **kwargs)

        if include_specs:
            return f"{base_desc}, CPU: {self.cpu_type}, RAM: {self.ram_gb}GB"
        return base_desc

    def run_diagnostics(self, *args, **kwargs):
        """A method specific to Computer that can also accept flexible arguments."""
        print(f"\nRunning diagnostics for Computer {self.asset_id}...")
        if "test_level" in kwargs:
            print(f"  Test Level: {kwargs['test_level']}")
        if args:
            print(f"  Diagnostic args: {args}")
        print(f"  Diagnostics for {self.cpu_type} with {self.ram_gb}GB RAM complete.")


# --- Example Usage ---
if __name__ == "__main__":
    print("Creating a generic asset with extra keyword arguments:")
    generic_asset = Asset(
        "A001",
        "2024-01-15",
        "extra_pos_1",  # Goes into *args in Asset.__init__
        location="Main Office",
        condition="New",
    )
    # location & condition go into **kwargs in Asset.__init__

    print("\nCreating a Computer with specific and extra arguments:")
    # 'asset_id', 'purchase_date', 'cpu_type', 'ram_gb' are explicitly named in Computer.__init__
    # 'extra_pos_sub' will be caught by *args in Computer.__init__ and passed to Asset's *args
    # 'department', 'user', 'fast_boot' will be caught by **kwargs in Computer.__init__
    # and passed to Asset's **kwargs (and stored in generic_asset.additional_info)
    my_laptop = Computer(
        "C001",
        "2025-01-20",
        "Intel i9",
        32,
        "extra_pos_sub",  # This goes into *args for Asset
        department="IT",
        user="Bassey",
        fast_boot=True,
    )  # These go into **kwargs for Asset

    print("\nGetting descriptions:")
    print(f"Generic Asset Desc: {generic_asset.get_description(short_desc=True)}")
    print(
        f"Laptop Desc (full): {my_laptop.get_description(include_specs=True, short_desc=False)}"
    )
    print(
        f"Laptop Desc (short from parent): {my_laptop.get_description(include_specs=False, short_desc=True)}"
    )
    print(
        f"Laptop Desc (with extra method args): {my_laptop.get_description('detail_mode', color_profile='sRGB')}"
    )

    print("\nRunning Computer-specific method:")
    my_laptop.run_diagnostics("quick_scan", test_level="Comprehensive")

    # Example showing how Asset's **kwargs are stored
    print(f"\nAdditional info stored in my_laptop (from Asset's **kwargs):")
    print(my_laptop.additional_info)
    print(f"Extra positional args in my_laptop (from Asset's *args):")
    print(my_laptop.extra_positional_args)
