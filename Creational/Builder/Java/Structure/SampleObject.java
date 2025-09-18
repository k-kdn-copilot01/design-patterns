package Creational.Builder.Java.Structure;

public class SampleObject {
    private String field1, field2, field3;

    public String getField1() {
        return field1;
    }

    public void setField1(String field1) {
        this.field1 = field1;
    }

    public String getField2() {
        return field2;
    }

    public void setField2(String field2) {
        this.field2 = field2;
    }

    public String getField3() {
        return field3;
    }

    public void setField3(String field3) {
        this.field3 = field3;
    }

    public static class Builder {
        private String field1, field2, field3;

        public Builder setField1(String field1) {
            this.field1 = field1;
            return this;
        }

        public Builder setField2(String field2) {
            this.field2 = field2;
            return this;
        }

        public Builder setField3(String field3) {
            this.field3 = field3;
            return this;
        }

        public SampleObject build() {
            SampleObject obj = new SampleObject();
            obj.setField1(field1);
            obj.setField2(field2);
            obj.setField3(field3);
            return obj;
        }
    }
}
