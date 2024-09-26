

#### English Version:

# Coffee Shop Website

**Author:** Matin Talkhbi

This project is a fully functional **Coffee Shop e-commerce website** built using Django and Tailwind CSS. It’s a professional-grade online store, designed as a model for any future e-commerce website. This version is a **prototype**, and the final version, once fully completed, will be uploaded to a new repository.

## Features:
- **Product Listings**: Display coffee products with images, descriptions, prices, and stock availability.
- **Shopping Cart**: Customers can add items to their cart, update quantities, and view the total price.
- **User Authentication**: Register, login, and manage user accounts for personalized shopping.
- **Payment Gateway Integration**: Secure online payment processing for easy transactions.
- **Order Management**: Track customer orders and update order statuses.
- **Responsive Design**: Fully responsive layout that adapts to any device (desktop, tablet, and mobile).
- **Admin Dashboard**: Manage products, categories, orders, and users through an intuitive admin interface.
- **Search & Filters**: Customers can search for products and filter by categories, price, or popularity.

## Technologies Used:
- **Django**: Backend framework for handling business logic, authentication, and database management.
- **Tailwind CSS**: For custom, responsive, and modern UI design.
- **SQLite**: For database management (can be easily switched to PostgreSQL or MySQL in the final version).
- **JavaScript**: For interactive elements such as cart updates and form validations.
- **Stripe API**: Integrated for handling secure online payments.
  
## How to Use:
1. Clone the repository:
    ```bash
    git clone https://github.com/yourusername/coffee-shop.git
    ```
2. Navigate to the project directory and set up the virtual environment:
    ```bash
    cd coffee-shop
    python -m venv env
    source env/bin/activate  # (On Windows: env\Scripts\activate)
    ```
3. Install dependencies:
    ```bash
    pip install -r requirements.txt
    ```
4. Run database migrations:
    ```bash
    python manage.py migrate
    ```
5. Start the development server:
    ```bash
    python manage.py runserver
    ```
6. Visit `http://localhost:8000` to view the website.

## Future Development:
- **Enhanced User Profiles**: Adding wishlists, order history, and saved addresses.
- **Inventory Management**: Advanced stock tracking and supplier integration.
- **Advanced Filters**: More comprehensive filtering options such as flavor profiles or brewing methods.
- **Full Version Release**: The full version of the website will be uploaded to a new repository once fully developed.

---

#### نسخه فارسی:

# وب‌سایت فروشگاه قهوه

**نویسنده:** متین تلخ‌بی

این پروژه یک **وب‌سایت فروشگاهی قهوه** است که به صورت کاملاً حرفه‌ای با استفاده از جنگو و تیلویند CSS ساخته شده است. این وب‌سایت به عنوان یک نمونه کامل از یک فروشگاه آنلاین طراحی شده و قابل استفاده برای هر نوع وب‌سایت فروشگاهی دیگر می‌باشد. این نسخه به عنوان **نمونه اولیه** ارائه شده است و نسخه نهایی پس از تکمیل به یک ریپازیتوری جدید آپلود خواهد شد.

## امکانات:
- **فهرست محصولات**: نمایش محصولات قهوه همراه با تصاویر، توضیحات، قیمت و موجودی.
- **سبد خرید**: کاربران می‌توانند محصولات را به سبد خرید اضافه کرده، تعداد را تغییر دهند و مبلغ کل را مشاهده کنند.
- **احراز هویت کاربر**: امکان ثبت‌نام، ورود و مدیریت حساب‌های کاربری برای خرید شخصی‌سازی‌شده.
- **درگاه پرداخت**: ادغام با درگاه پرداخت امن برای انجام تراکنش‌های آنلاین.
- **مدیریت سفارشات**: پیگیری سفارشات مشتریان و به‌روزرسانی وضعیت سفارش.
- **طراحی ریسپانسیو**: طراحی کاملاً واکنش‌گرا که به راحتی روی هر دستگاهی (دسکتاپ، تبلت و موبایل) نمایش داده می‌شود.
- **داشبورد مدیریت**: مدیریت محصولات، دسته‌بندی‌ها، سفارشات و کاربران از طریق یک رابط مدیریتی آسان.
- **جستجو و فیلتر**: کاربران می‌توانند محصولات را جستجو کرده و بر اساس دسته‌بندی، قیمت یا محبوبیت فیلتر کنند.

## تکنولوژی‌های استفاده شده:
- **جنگو**: فریم‌ورک بک‌اند برای مدیریت منطق تجاری، احراز هویت و مدیریت پایگاه داده.
- **تیلویند CSS**: برای طراحی رابط کاربری سفارشی، مدرن و ریسپانسیو.
- **SQLite**: برای مدیریت پایگاه داده (که در نسخه نهایی به راحتی می‌تواند به PostgreSQL یا MySQL تغییر کند).
- **جاوااسکریپت**: برای عناصر تعاملی مانند به‌روزرسانی سبد خرید و اعتبارسنجی فرم‌ها.
- **Stripe API**: برای پردازش امن پرداخت‌های آنلاین.

## نحوه استفاده:
1. ریپازیتوری را کلون کنید:
    ```bash
    git clone https://github.com/yourusername/coffee-shop.git
    ```
2. به دایرکتوری پروژه رفته و محیط مجازی را راه‌اندازی کنید:
    ```bash
    cd coffee-shop
    python -m venv env
    source env/bin/activate  # (برای ویندوز: env\Scripts\activate)
    ```
3. وابستگی‌ها را نصب کنید:
    ```bash
    pip install -r requirements.txt
    ```
4. مایگریشن‌های پایگاه داده را اجرا کنید:
    ```bash
    python manage.py migrate
    ```
5. سرور توسعه را راه‌اندازی کنید:
    ```bash
    python manage.py runserver
    ```
6. وب‌سایت را در آدرس `http://localhost:8000` مشاهده کنید.

## توسعه آینده:
- **پروفایل‌های کاربری پیشرفته**: اضافه کردن لیست علاقه‌مندی‌ها، تاریخچه سفارشات و آدرس‌های ذخیره‌شده.
- **مدیریت موجودی**: پیگیری پیشرفته موجودی و ادغام با تأمین‌کنندگان.
- **فیلترهای پیشرفته**: اضافه کردن گزینه‌های فیلتر بیشتر مانند پروفایل طعم‌ها یا روش‌های دم‌آوری.
- **انتشار نسخه کامل**: نسخه نهایی وب‌سایت پس از تکمیل در یک ریپازیتوری جدید آپلود خواهد شد.

---

