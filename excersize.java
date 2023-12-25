package exam;

import java.util.*;

public class excersize {
    static Set<Notebook> notebooks = new HashSet<>();
    static HashMap<String, String> filters = new HashMap<>();

    public static void main(String[] args) throws InterruptedException {
        Scanner scanner = new Scanner(System.in);
        int mode = 1;
        init();

        System.out.println("1 - показать все ноутбуки");
        System.out.println("2 - отфильтровать и показать ноутбуки");
        System.out.println("3 - выход");
        mode = scanner.nextInt();
        switch (mode) {
            case 1:
                System.out.println(notebooks);
                break;
            case 2:
                System.out.println("Объем ОЗУ: ");
                filters.put("ozu", scanner.nextLine());
                System.out.println("Объем ЖД: ");
                filters.put("hdd", scanner.nextLine());
                System.out.println("ОС: ");
                filters.put("os", scanner.nextLine());
                System.out.println("Цвет: ");
                filters.put("color", scanner.nextLine());
                System.out.println("Процессор: ");
                filters.put("cpu", scanner.nextLine());
                System.out.println("Видеокарта: ");
                filters.put("gpu", scanner.nextLine());
                System.out.println(filters);
                if (!filters.get("ozu").isEmpty()) {
                    notebooks.removeIf(x -> x.getOzu() < Integer.parseInt(filters.get("ozu")));
                }
                if (!filters.get("hdd").isEmpty()) {
                    notebooks.removeIf(x -> x.getHdd() < Integer.parseInt(filters.get("hdd")));
                }
                if (!filters.get("os").isEmpty()) {
                    notebooks.removeIf(x -> !x.getOs().contains(filters.get("os")));
                }
                if (!filters.get("color").isEmpty()) {
                    notebooks.removeIf(x -> !x.getColor().equals(filters.get("color")));
                }
                if (!filters.get("cpu").isEmpty()) {
                    notebooks.removeIf(x -> !x.getCpu().equals(filters.get("cpu")));
                }
                if (!filters.get("gpu").isEmpty()) {
                    notebooks.removeIf(x -> !x.getGpu().contains(filters.get("gpu")));
                }
                System.out.println(notebooks);
                break;
            default:
                System.out.println("До свидания!");
        }
    }


    static void init() {
        notebooks.add(new Notebook(8, 1000, "Win11", "Black", "i5-9400F", "RTX2060"));
        notebooks.add(new Notebook(8, 1000, "Win10", "Black", "i7-7700Q", "GTX1070Ti"));
        notebooks.add(new Notebook(16, 2000, "Win11", "Silver", "i7-13700K", "RTX3060"));
        notebooks.add(new Notebook(16, 512, "Win11", "Grey", "R7-7725HS", "RTX4050"));
    }
}

class Notebook {
    private final int ozu;
    private final int hdd;
    private final String os;
    private final String color;
    private final String cpu;
    private final String gpu;

    public Notebook(int ozu, int hdd, String os, String color, String cpu, String gpu) {
        this.ozu = ozu;
        this.hdd = hdd;
        this.os = os;
        this.color = color;
        this.cpu = cpu;
        this.gpu = gpu;
    }

    public int getOzu() {
        return ozu;
    }

    public int getHdd() {
        return hdd;
    }

    public String getOs() {
        return os;
    }

    public String getColor() {
        return color;
    }

    public String getCpu() {
        return cpu;
    }

    public String getGpu() {
        return gpu;
    }

    @Override
    public String toString() {
        return "Notebook{" +
                "ozu=" + ozu +
                ", hdd=" + hdd +
                ", os='" + os + '\'' +
                ", color='" + color + '\'' +
                ", cpu='" + cpu + '\'' +
                ", gpu='" + gpu + '\'' +
                '}';
    }
}
