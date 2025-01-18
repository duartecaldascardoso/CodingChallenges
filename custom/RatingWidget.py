class RatingWidget:
    @staticmethod
    def render(current_rating):
        return f"""
        <style>
        .rating-container {{
            position: absolute;
            top: 40px;
            right: 10px;
            padding: 10px 15px;
            border-radius: 5px;
            border: 2px solid #ffffff;
            font-weight: bold;
            color: #ffffff;
            background-color: transparent;
        }}
        </style>
        <div class="rating-container">
            Current Rating: {current_rating}
        </div>
        """